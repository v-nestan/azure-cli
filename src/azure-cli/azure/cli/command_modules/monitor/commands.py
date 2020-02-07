# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


# pylint: disable=line-too-long, too-many-locals, too-many-statements
def load_command_table(self, _):

    from ._client_factory import (
        cf_alert_rules, cf_metric_def, cf_alert_rule_incidents, cf_log_profiles, cf_autoscale,
        cf_diagnostics, cf_activity_log, cf_action_groups, cf_activity_log_alerts, cf_event_categories,
        cf_metric_alerts, cf_log_analytics_workspace, cf_diagnostics_category)
    from ._exception_handler import monitor_exception_handler, missing_resource_handler
    from .transformers import (action_group_list_table)
    from .validators import process_autoscale_create_namespace

    monitor_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.monitor.custom#{}',
        exception_handler=monitor_exception_handler)

    action_group_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#ActionGroupsOperations.{}',
        client_factory=cf_action_groups,
        operation_group='action_groups',
        exception_handler=monitor_exception_handler)

    action_group_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.monitor.operations.action_groups#{}',
        client_factory=cf_action_groups,
        operation_group='action_groups',
        exception_handler=monitor_exception_handler)

    activity_log_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#EventCategoriesOperations.{}',
        client_factory=cf_event_categories,
        operation_group='event_categories',
        exception_handler=monitor_exception_handler)

    activity_log_alerts_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#ActivityLogAlertsOperations.{}',
        client_factory=cf_activity_log_alerts,
        operation_group='activity_log_alerts',
        exception_handler=monitor_exception_handler)

    activity_log_alerts_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.monitor.operations.activity_log_alerts#{}',
        client_factory=cf_activity_log_alerts,
        operation_group='activity_log_alerts',
        exception_handler=monitor_exception_handler)

    alert_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#AlertRulesOperations.{}',
        client_factory=cf_alert_rules,
        operation_group='alert_rules',
        exception_handler=monitor_exception_handler)

    alert_rule_incidents_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#AlertRuleIncidentsOperations.{}',
        client_factory=cf_alert_rule_incidents,
        operation_group='alert_rule_incidents',
        exception_handler=monitor_exception_handler)

    autoscale_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#AutoscaleSettingsOperations.{}',
        client_factory=cf_autoscale,
        operation_group='autoscale_settings',
        exception_handler=monitor_exception_handler)

    autoscale_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.monitor.operations.autoscale_settings#{}',
        client_factory=cf_autoscale,
        operation_group='autoscale_settings',
        exception_handler=monitor_exception_handler)

    diagnostics_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#DiagnosticSettingsOperations.{}',
        client_factory=cf_diagnostics,
        operation_group='diagnostic_settings',
        exception_handler=monitor_exception_handler)

    diagnostics_categories_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#DiagnosticSettingsCategoryOperations.{}',
        client_factory=cf_diagnostics_category,
        operation_group='diagnostic_settings_category',
        exception_handler=monitor_exception_handler)

    diagnostics_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.monitor.operations.diagnostics_settings#{}',
        client_factory=cf_diagnostics,
        operation_group='diagnostic_settings_category',
        exception_handler=monitor_exception_handler)

    log_profiles_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#LogProfilesOperations.{}',
        client_factory=cf_log_profiles,
        operation_group='log_profiles',
        exception_handler=monitor_exception_handler)

    log_profiles_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.monitor.operations.log_profiles#{}',
        client_factory=cf_log_profiles,
        operation_group='log_profiles',
        exception_handler=monitor_exception_handler)

    alert_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.monitor.operations.metric_alert#{}',
        client_factory=cf_alert_rules,
        operation_group='alert_rules',
        exception_handler=monitor_exception_handler)

    metric_alert_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#MetricAlertsOperations.{}',
        client_factory=cf_metric_alerts,
        operation_group='metric_alerts',
        exception_handler=monitor_exception_handler)

    metric_definitions_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.monitor.operations#MetricDefinitionsOperations.{}',
        client_factory=cf_metric_def,
        operation_group='metric_definitions',
        exception_handler=monitor_exception_handler)

    log_analytics_workspace_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.loganalytics.operations#WorkspacesOperations.{}',
        client_factory=cf_log_analytics_workspace,
        exception_handler=monitor_exception_handler
    )

    log_analytics_workspace_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.monitor.operations.log_analytics_workspace#{}',
        client_factory=cf_log_analytics_workspace,
        exception_handler=monitor_exception_handler
    )

    with self.command_group('monitor action-group', action_group_sdk, custom_command_type=action_group_custom) as g:
        g.show_command('show', 'get', table_transformer=action_group_list_table)
        g.command('create', 'create_or_update', table_transformer=action_group_list_table)
        g.command('delete', 'delete')
        g.command('enable-receiver', 'enable_receiver', table_transformer=action_group_list_table)
        g.custom_command('list', 'list_action_groups', table_transformer=action_group_list_table)
        g.generic_update_command('update', custom_func_name='update_action_groups', setter_arg_name='action_group',
                                 table_transformer=action_group_list_table)

    with self.command_group('monitor activity-log', activity_log_sdk) as g:
        g.custom_command('list', 'list_activity_log', client_factory=cf_activity_log)
        g.command('list-categories', 'list')

    with self.command_group('monitor activity-log alert', activity_log_alerts_sdk, custom_command_type=activity_log_alerts_custom) as g:
        g.custom_command('list', 'list_activity_logs_alert')
        g.custom_command('create', 'create')
        g.show_command('show', 'get', exception_handler=missing_resource_handler)
        g.command('delete', 'delete', exception_handler=missing_resource_handler)
        g.generic_update_command('update', custom_func_name='update', setter_arg_name='activity_log_alert')
        g.custom_command('action-group add', 'add_action_group')
        g.custom_command('action-group remove', 'remove_action_group')
        g.custom_command('scope add', 'add_scope')
        g.custom_command('scope remove', 'remove_scope')

    with self.command_group('monitor alert', alert_sdk, custom_command_type=alert_custom, deprecate_info=self.deprecate(redirect='monitor metrics alert', hide='2.0.44')) as g:
        g.custom_command('create', 'create_metric_rule')
        g.command('delete', 'delete')
        g.show_command('show', 'get')
        g.command('list', 'list_by_resource_group')
        g.command('show-incident', 'get', command_type=alert_rule_incidents_sdk)
        g.command('list-incidents', 'list_by_alert_rule', command_type=alert_rule_incidents_sdk)
        g.generic_update_command('update', custom_func_name='update_metric_rule')

    with self.command_group('monitor autoscale', autoscale_sdk, custom_command_type=autoscale_custom) as g:
        g.custom_command('create', 'autoscale_create', validator=process_autoscale_create_namespace)
        g.generic_update_command('update', custom_func_name='autoscale_update', custom_func_type=autoscale_custom,
                                 exception_handler=monitor_exception_handler)
        g.command('delete', 'delete')
        g.show_command('show', 'get')
        g.command('list', 'list_by_resource_group')

    with self.command_group('monitor autoscale profile', autoscale_sdk, custom_command_type=autoscale_custom) as g:
        g.custom_command('create', 'autoscale_profile_create')
        g.custom_command('list', 'autoscale_profile_list')
        g.custom_show_command('show', 'autoscale_profile_show')
        g.custom_command('delete', 'autoscale_profile_delete')
        g.custom_command('list-timezones', 'autoscale_profile_list_timezones')

    with self.command_group('monitor autoscale rule', autoscale_sdk, custom_command_type=autoscale_custom) as g:
        g.custom_command('create', 'autoscale_rule_create')
        g.custom_command('list', 'autoscale_rule_list')
        g.custom_command('delete', 'autoscale_rule_delete')
        g.custom_command('copy', 'autoscale_rule_copy')

    with self.command_group('monitor autoscale-settings', autoscale_sdk, custom_command_type=autoscale_custom,
                            deprecate_info=self.deprecate(redirect='monitor autoscale', hide='2.0.34')) as g:
        g.command('create', 'create_or_update', deprecate_info='az monitor autoscale create')
        g.command('delete', 'delete', deprecate_info='az monitor autoscale delete')
        g.show_command('show', 'get', deprecate_info='az monitor autoscale show')
        g.command('list', 'list_by_resource_group', deprecate_info='az monitor autoscale list')
        g.custom_command('get-parameters-template', 'scaffold_autoscale_settings_parameters', deprecate_info='az monitor autoscale show')
        g.generic_update_command('update', deprecate_info='az monitor autoscale update')

    with self.command_group('monitor diagnostic-settings', diagnostics_sdk, custom_command_type=diagnostics_custom) as g:
        from .validators import validate_diagnostic_settings
        g.custom_command('create', 'create_diagnostics_settings', validator=validate_diagnostic_settings)
        g.show_command('show', 'get')
        g.command('list', 'list')
        g.command('delete', 'delete')
        g.generic_update_command('update')

    with self.command_group('monitor diagnostic-settings categories', diagnostics_categories_sdk) as g:
        g.show_command('show', 'get')
        g.command('list', 'list')

    with self.command_group('monitor log-profiles', log_profiles_sdk, custom_command_type=log_profiles_custom) as g:
        g.custom_command('create', 'create_log_profile_operations')
        g.command('delete', 'delete')
        g.show_command('show', 'get')
        g.command('list', 'list')
        g.generic_update_command('update')

    with self.command_group('monitor metrics') as g:
        from .transformers import metrics_table, metrics_definitions_table
        g.command('list', 'list_metrics', command_type=monitor_custom, table_transformer=metrics_table)
        g.command('list-definitions', 'list', command_type=metric_definitions_sdk, table_transformer=metrics_definitions_table)

    with self.command_group('monitor metrics alert', metric_alert_sdk, custom_command_type=alert_custom, client_factory=cf_metric_alerts) as g:
        g.custom_command('create', 'create_metric_alert', custom_command_type=alert_custom)
        g.command('delete', 'delete')
        g.custom_command('list', 'list_metric_alerts', custom_command_type=alert_custom)
        g.command('show', 'get')
        g.generic_update_command('update', custom_func_name='update_metric_alert', custom_func_type=alert_custom)

    with self.command_group('monitor log-analytics workspace', log_analytics_workspace_sdk, custom_command_type=log_analytics_workspace_custom, is_preview=True) as g:
        g.custom_command('create', 'create_log_analytics_workspace')
        g.generic_update_command('update', custom_func_name='update_log_analytics_workspace')
        g.command('show', 'get')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_log_analytics_workspace')
        g.command('get-schema', 'get_schema')
        g.command('list-usages', 'list_usages')
        g.command('list-management-groups', 'list_management_groups')
        g.command('get-shared-keys', 'get_shared_keys')

    with self.command_group('monitor log-analytics workspace pack', log_analytics_workspace_sdk, custom_command_type=log_analytics_workspace_custom) as g:
        g.command('list', 'list_intelligence_packs')
        g.command('enable', 'enable_intelligence_pack')
        g.command('disable', 'disable_intelligence_pack')
