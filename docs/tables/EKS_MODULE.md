# EKS_MODULE

> The module header record. Defines base expert module attributes.

**Description:** EKS Module  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_FLAG` | CHAR(1) | NOT NULL |  | When eks modules are saved, their active flag is set to 'A' (Active) and all other versions of the same module are made 'I' (inactive). |
| 2 | `EKS_RELEASE` | CHAR(10) |  |  | This field indicates the release of the EKS system that created the module. If the release is less than the current release being used, this module's format will change to the new format when re-saved. If loaded with a prior version of the EKM editor, then the load MAY succeed, or it may fail, in any case, the module will NEVER allowed to be changed with a prior version of the EKM Editor. |
| 3 | `KNOW_PRIORITY` | DOUBLE |  |  | The module's priority when executing in the expert server. |
| 4 | `KNOW_TYPE` | CHAR(20) |  |  | The type of the module. DATA_DRIVEN, GOAL_DRIVEN, TIME_DRIVEN |
| 5 | `KNOW_URGENCY` | DOUBLE |  |  | The priority of the action section of the module. |
| 6 | `LAST_REV_DT_TM` | DATETIME |  |  | The date the module had a significant change, as determined by the module editor. May differ from if the compile was not deemed significant. User defined field. |
| 7 | `MAINT_AUTHOR` | VARCHAR(255) |  |  | The author of the module. |
| 8 | `MAINT_DATE` | DATETIME |  |  | date the module was created. |
| 9 | `MAINT_DUR_BEGIN_DT_TM` | DATETIME |  |  | The beginning of the time frame when the module should be active. |
| 10 | `MAINT_DUR_END_DT_TM` | DATETIME |  |  | the end of the module active time frame. |
| 11 | `MAINT_FILENAME` | VARCHAR(30) |  |  | The file name used to contain the source text of the eks module. |
| 12 | `MAINT_INSTITUTION` | VARCHAR(255) |  |  | The institution using the expert module. |
| 13 | `MAINT_SPECIALIST` | VARCHAR(255) |  |  | The person responsible for encoding the knowledge represented by this ekm. |
| 14 | `MAINT_TITLE` | VARCHAR(255) |  |  | The title of the module as free text. |
| 15 | `MAINT_VALIDATION` | CHAR(12) |  |  | The level of validation this module has been through. |
| 16 | `MAINT_VERSION` | CHAR(10) |  |  | Version of the module. The version is incremented every time the module is saved. |
| 17 | `MODULE_NAME` | CHAR(30) | NOT NULL |  | The name of the module. |
| 18 | `NUM_STORAGE` | DOUBLE |  |  | The number of eks_modulestorage records required to store the module definition. |
| 19 | `OPTIMIZED_IND` | DOUBLE | NOT NULL |  | Optimized Indicator for current module version. 0 = No values were optimized, 1 = At least one parameter value was optimized. |
| 20 | `OPTIMIZE_FLAG` | DOUBLE | NOT NULL |  | Module Optimization Flag. 0 - System default value. 1 - Optimizes the module.2 - Don¿t optimizes the module. |
| 21 | `RECONCILE_DT_TM` | DATETIME |  |  | The date of the module reconciled. |
| 22 | `RECONCILE_FLAG` | DOUBLE | NOT NULL |  | Module Reconciliation Status Flag. 0 = Reconciliation not attempted on current module version , 1 = Module was fully reconcilable with no exceptions found, 2 = Reconciliation exceptions were found, 3 = Module was only partially reconcilable, but no exceptions were found3 - Attempt made. Patial was Ok |
| 23 | `RELEASE_DT_TM` | DATETIME |  |  | The date that action(s) are seen on the front end by users. May differ from if testing was done before releasing the module to end users. User defined field. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `VERSION` | CHAR(10) | NOT NULL |  | version assigned to module to keep track of latest module saved since previous modules are retained. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

