# ENCNTR_TYPE_PARAMS

> Reference table using name value pair logic at the encntr_type_cd and organization_id level. This table is similar to the 150 table in HNA 306.

**Description:** Encounter Type Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `COLLATION_SEQ` | DOUBLE |  |  | Defines the order in which the name value pair attributes will show in the encntr_type_maint tool. |
| 3 | `ENCNTR_TYPE_CD` | DOUBLE |  |  | Defines the type of encounter (Inpatient, Outpatient, etc.) -- used in this table to separate parameters using name value pair logic. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ORGANIZATION_ID` | DOUBLE |  |  | Foreign key to the ORGANIZATION table defines along with encntr_type_cd the separate rows for the name value pair logic |
| 6 | `PARAM_NAME` | VARCHAR(32) |  |  | The name of the name value pair field. |
| 7 | `VALUE_CD` | DOUBLE |  |  | The value related to the PARAM_NAME attribute. Shows here only if it is a codified value. Code set will vary. |
| 8 | `VALUE_DT_TM` | DATETIME |  |  | The value related to the PARAM_NAME attribute. Filled out only if it is of date/time type. |
| 9 | `VALUE_IND` | DOUBLE |  |  | The value relating to the PARAM_NAME attribute. Is filled out only if it is of type indicator. |
| 10 | `VALUE_NBR` | DOUBLE |  |  | The value related to the PARAM_NAME attribute. This is valued only if it is of type number and not a flag or indicator. |
| 11 | `VALUE_STRING` | VARCHAR(200) |  |  | The value related to the PARAM_NAME attribute. This is valued only if it is of type string. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

