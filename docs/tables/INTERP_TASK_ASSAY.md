# INTERP_TASK_ASSAY

> The procedure defined as being an interpretation of the results entered for other procedures.

**Description:** Interpretation Task Assay  
**Table type:** REFERENCE  
**Primary key:** `INTERP_ID`  
**Columns:** 17  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `GENERATE_INTERP_FLAG` | DOUBLE |  |  | Determines if interp is automatically entered (system generated) by the system or if the user is to fill out the interp value but the system validates the entered result. |
| 6 | `INTERP_ID` | DOUBLE | NOT NULL | PK | An internal system-assigned number that ensures the uniqueness of each row on this table. |
| 7 | `INTERP_OPTION_CD` | DOUBLE | NOT NULL |  | Determines if the result can be modified, read-only, or non-viewable. |
| 8 | `INTERP_TYPE_CD` | DOUBLE | NOT NULL |  | Determines the type of result. Possible choices can be alpha, textual, numerical, and codeset list. |
| 9 | `ORDER_CAT_CD` | DOUBLE | NOT NULL | FK→ | Used to store the internal code for the order catalog item |
| 10 | `PHASE_CD` | DOUBLE | NOT NULL |  | Field no longer used |
| 11 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | A unique internal identifier for this service resource |
| 12 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | The code value for the task/assay |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_CAT_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [INTERP_COMPONENT](INTERP_COMPONENT.md) | `INTERP_ID` |
| [INTERP_RANGE](INTERP_RANGE.md) | `INTERP_ID` |
| [INTERP_RESULT](INTERP_RESULT.md) | `INTERP_ID` |
| [RESULT_HASH](RESULT_HASH.md) | `INTERP_ID` |

