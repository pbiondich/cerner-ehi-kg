# SA_REF_ACTION

> Contains all of the actions that can be documented within an anesthesia record. Size - Based on the number of actions that are built. Estimate < 100 rows.

**Description:** SA Reference Action  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_ACTION_ID`  
**Columns:** 30  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DESCRIPTION` | VARCHAR(250) |  |  | Unique value that identifies the action |
| 2 | `ACTION_NAME` | VARCHAR(30) |  |  | Display name of the action |
| 3 | `ACTION_NAME_KEY` | VARCHAR(50) |  |  | Display name of the action upper case with no blanks. |
| 4 | `ACTION_NAME_KEY_A_NLS` | VARCHAR(200) |  |  | ACTION_NAME_KEY_A_NLS column |
| 5 | `ACTION_NAME_KEY_NLS` | VARCHAR(102) |  |  | Display name of the action _key_nls format |
| 6 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 9 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 10 | `BILL_IND` | DOUBLE | NOT NULL |  | Indicates whether action should be displayed on the billing summary |
| 11 | `CHILD_SELECTION_REQ_IND` | DOUBLE | NOT NULL |  | Indicates whether a value has to be entered for the action when it is documented |
| 12 | `DEFAULT_VALUE` | VARCHAR(250) |  |  | Default Value |
| 13 | `ORIGINAL_REF_ACTION_ID` | DOUBLE | NOT NULL | FK→ | FK from the original SA_REF_ACTION_ID value. Used for versioning. |
| 14 | `PRINT_IND` | DOUBLE | NOT NULL |  | Indicates whether action detail for group should be displayed on the billing summary |
| 15 | `REF_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of reference this item is built for (I.e Anesthesia (0), CVNet (1) |
| 16 | `REMINDER_FREQUENCY_MINS` | DOUBLE |  |  | The interval in minutes which represents the default value of frequency of the reminder associated to an action. |
| 17 | `SA_REF_ACTION_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the action Primary Key |
| 18 | `SA_REF_ICON_ID` | DOUBLE | NOT NULL | FK→ | The icon associated with the action it |
| 19 | `SIGNATURE_REQUIRED_IND` | DOUBLE | NOT NULL |  | Determines if action signature is required |
| 20 | `SINGLE_DOC_IND` | DOUBLE | NOT NULL |  | Defines whether the action can be documented multiple times or only once per record |
| 21 | `SUPERVISOR_SIGN_REQ_IND` | DOUBLE | NOT NULL |  | The supervisor_sign_req_ind is set to '1' if supervisor signature is required on the action, else it is set to '0' |
| 22 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay Code - code set 14003 |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `VALUE_REQUIRED_IND` | DOUBLE |  |  | Indicates whether a value has to be entered for the action when it is documented (1=value must be entered,0=a value doesn't have to be entered) |
| 29 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | The type of value that can be entered for this action |
| 30 | `VERSION_NBR` | DOUBLE | NOT NULL |  | Version Number. Used for Versioning. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIGINAL_REF_ACTION_ID` | [SA_REF_ACTION](SA_REF_ACTION.md) | `SA_REF_ACTION_ID` |
| `SA_REF_ICON_ID` | [SA_REF_ICON](SA_REF_ICON.md) | `SA_REF_ICON_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [SA_ACTION](SA_ACTION.md) | `SA_REF_ACTION_ID` |
| [SA_REF_ACTION](SA_REF_ACTION.md) | `ORIGINAL_REF_ACTION_ID` |
| [SA_REF_ACTION_GROUP_R](SA_REF_ACTION_GROUP_R.md) | `SA_REF_ACTION_ID` |
| [SA_REF_CAT_ACTION](SA_REF_CAT_ACTION.md) | `SA_REF_ACTION_ID` |
| [SA_REF_EXCLUDE_ACTION](SA_REF_EXCLUDE_ACTION.md) | `SA_REF_ACTION_ID` |
| [SA_REF_MACRO_ACTION](SA_REF_MACRO_ACTION.md) | `SA_REF_ACTION_ID` |
| [SA_REF_REQUIRED_ACTION](SA_REF_REQUIRED_ACTION.md) | `SA_REF_ACTION_ID` |
| [SA_TODO_ACTION](SA_TODO_ACTION.md) | `SA_REF_ACTION_ID` |

