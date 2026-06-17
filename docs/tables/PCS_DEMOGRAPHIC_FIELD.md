# PCS_DEMOGRAPHIC_FIELD

> Cerner defined reference data. Contains definitions for fields available in the customizable demographics display.

**Description:** PathNet Demographic Fields  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLATION_NAME` | VARCHAR(60) | NOT NULL |  | Specifies the name used in a sorted list. |
| 2 | `CURRENT_FIELD_CD` | DOUBLE | NOT NULL | FK→ | For historical fields, this specifies the corresponding current field. May be 0 if there is no corresponding current field. For current fields, this is always 0.The data model also allows for an "historic" field that does not have a corresponding current field. In this case, HISTORICAL_IND would be "1", but CURRENT_FIELD_CD would be "0". |
| 3 | `DEFAULT_LABEL_TEXT` | VARCHAR(60) |  |  | Default Label text field |
| 4 | `FIELD_CD` | DOUBLE | NOT NULL | FK→ | The field this row corresponds to. |
| 5 | `HISTORICAL_IND` | DOUBLE | NOT NULL |  | two demographic fields that contain similar information, except the one represents the "current" value, and one represents the "historic" value. For example, one row in the table will be "Patient Name", and another row will be "Historical Patient Name". Logic requires that we do some special handling when this kind of relationship exists. We represent this by having the "Historical" row point to the "Current" row using the CURRENT_FIELD_CD. In this case the "HISTORICAL_IND will = 1. |
| 6 | `PREVIEW_TEXT` | VARCHAR(200) |  |  | Canned text to be displayed as data for this field when previewing layout. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CURRENT_FIELD_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FIELD_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

