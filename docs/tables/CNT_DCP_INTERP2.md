# CNT_DCP_INTERP2

> CONTENT DCP INTERPRET

**Description:** CNT DCP INTERP  
**Table type:** REFERENCE  
**Primary key:** `CNT_DCP_INTERP2_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_FROM_MINUTES` | DOUBLE | NOT NULL |  | defines the beginning age range defined for the calculation. |
| 2 | `AGE_TO_MINUTES` | DOUBLE | NOT NULL |  | defines the ending age range defined for the calculation. |
| 3 | `CNT_DCP_INTERP2_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `CNT_DTA_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) |
| 5 | `DCP_INTERP_ID` | DOUBLE | NOT NULL |  | Unique identifier for Interp |
| 6 | `DCP_INTERP_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Interp |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Code Set: 221 a unique code value that identifies the service resource associated with the equation. a value of zero means all service resources. |
| 8 | `SERVICE_RESOURCE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Service Resource Code Value |
| 9 | `SEX_CD` | DOUBLE | NOT NULL |  | Code Set: 57 a unique code value that identifies the sex of the person for which the equation is to be used. |
| 10 | `SEX_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Sex Code Value |
| 11 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_DTA_KEY_ID` | [CNT_DTA_KEY2](CNT_DTA_KEY2.md) | `CNT_DTA_KEY_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CNT_DCP_INTERP_COMPONENT](CNT_DCP_INTERP_COMPONENT.md) | `CNT_DCP_INTERP_ID` |
| [CNT_DCP_INTERP_STATE](CNT_DCP_INTERP_STATE.md) | `CNT_DCP_INTERP_ID` |

