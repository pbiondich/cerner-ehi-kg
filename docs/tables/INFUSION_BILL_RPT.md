# INFUSION_BILL_RPT

> To store the report information for Infusion Billing of an patient encounter.

**Description:** Infusion Billing Report  
**Table type:** ACTIVITY  
**Primary key:** `INFUSION_BILL_RPT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE |  | FK→ | Identifies the encounter for the billig report |
| 2 | `END_DT_TM` | DATETIME |  |  | The date and time the medication administration ended.; |
| 3 | `INFUSION_BILL_RPT_ID` | DOUBLE | NOT NULL | PK | THE PRIMARY KEY |
| 4 | `PERFORMED_DT_TM` | DATETIME |  |  | Date and time the action was performed for the billing report |
| 5 | `PERFORMED_PRSNL_ID` | DOUBLE |  | FK→ | the personnel performing the encounter process |
| 6 | `START_DT_TM` | DATETIME |  |  | the date and time the medication administration was started.; |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `VALID_UNTIL_DT_TM` | DATETIME |  |  | The valid date and time of a Infusion Billing Report.; |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERFORMED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INFUSION_BILL_RPT_ADMIN](INFUSION_BILL_RPT_ADMIN.md) | `INFUSION_BILL_RPT_ID` |

