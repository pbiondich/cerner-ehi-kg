# HF_D_UNIT

> This is the HealthFacts dimension table that contains standard values for unit of measure

**Description:** HF_D_UNIT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `UCUM_IND` | DOUBLE |  |  | An indicator that will be used for the Health Data mapping tool to help find records that have a standard UCUM definition. |
| 2 | `UCUM_LONG_DESC` | VARCHAR(250) |  |  | The UCUM standard long description for the unit of measure. |
| 3 | `UNIT_DESC` | VARCHAR(60) |  |  | A description of the unit of measure. |
| 4 | `UNIT_DISPLAY` | VARCHAR(20) |  |  | The display of the unit of measure |
| 5 | `UNIT_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a unit of measure |
| 6 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 7 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, MANUAL should be entered. |
| 8 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

