# REGIMEN_ATTRIBUTE

> Storage for attributes captured for a regimen

**Description:** Regimen Attribute  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_DISPLAY` | VARCHAR(100) | NOT NULL |  | ATTRIBUTE_DISPLAY refers to the display name for the attribute. |
| 2 | `ATTRIBUTE_DISPLAY_FLAG` | DOUBLE | NOT NULL |  | Display mode for the attribute on the regimen 0 = Unknown 1 = Display Only 2 = Optional 3 = Required |
| 3 | `ATTRIBUTE_MEAN` | VARCHAR(12) | NOT NULL |  | ATTRIBUTE_MEAN refers to the display meaning for the attribute. RESEARCHPROT, TREATMENTINT, THERAPYLINE |
| 4 | `CODE_SET` | DOUBLE | NOT NULL |  | Holds the pre defined responses for attribute. |
| 5 | `INPUT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the input type for the attribute. 1-Yes/No 2-Codeset |
| 6 | `REGIMEN_ATTRIBUTE_ID` | DOUBLE | NOT NULL |  | sequence name: CareNet_seq Unique identifier for the REGIMEN_ATTRIBUTE table. |
| 7 | `REGIMEN_CAT_ATTRIBUTE_R_ID` | DOUBLE | NOT NULL | FK→ | FK FROM REGIMEN_CAT_ATTRIBUTE_R |
| 8 | `REGIMEN_ID` | DOUBLE | NOT NULL | FK→ | sequence name: CareNet_seq Unique identifier for the REGIMEN table. |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | REGIMEN ATTRIBUTE SEQUENCE |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALUE_ID` | DOUBLE | NOT NULL |  | indicates value from table (code value field) or application specific value (0 - No selection/1 - Yes/2 - No) identified in value_name (CODE_VALUE or BOOLEAN). |
| 16 | `VALUE_NAME` | VARCHAR(30) |  |  | VALUE_NAME - Indicates whether the value in value_id column refers to an actual entity in the database (i.e. CODE_VALUE) or an application-specific value (i.e. BOOLEAN). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REGIMEN_CAT_ATTRIBUTE_R_ID` | [REGIMEN_CAT_ATTRIBUTE_R](REGIMEN_CAT_ATTRIBUTE_R.md) | `REGIMEN_CAT_ATTRIBUTE_R_ID` |
| `REGIMEN_ID` | [REGIMEN](REGIMEN.md) | `REGIMEN_ID` |

