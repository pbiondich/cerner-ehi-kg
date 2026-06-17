# AP_SYS_CORR_DETAIL

> This reference table includes the trigger and lookback parameters established for system selected correlation events.

**Description:** System Selected Correlation Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOOKBACK_IND` | DOUBLE | NOT NULL |  | This indicator field is used to determine whether this parameter is a look back parameter or a trigger parameter. |
| 2 | `PARAM_NAME` | VARCHAR(20) | NOT NULL |  | This field contains the name of system correlation parameter. |
| 3 | `PARAM_SEQUENCE` | DOUBLE | NOT NULL |  | This field in used in conjunction with the PARAM_NAME column in order to identify a single correlation parameter. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the parameter. For example, if the PARAM_NAME is SPECIMEN then the PARENT_ENTITY_NAME would be CODE_VALUE and the PARENT_ENTITY_ID column would contain a code value from the specimen code set. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | This field indicates the name of table to which the PARENT_ENTITY_ID value is from. |
| 6 | `SYS_CORR_DETAIL_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code that uniquely identifies a row on this table. |
| 7 | `SYS_CORR_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the AP_SYS_CORR table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SYS_CORR_ID` | [AP_SYS_CORR](AP_SYS_CORR.md) | `SYS_CORR_ID` |

