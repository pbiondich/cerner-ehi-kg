# OSM_FORM_FIELDS

> Table used to store unique fields of different types for a specific Form.

**Description:** OSM FORM FIELDS  
**Table type:** REFERENCE  
**Primary key:** `FORM_FIELD_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISP_LEN` | DOUBLE |  |  | User defined length a given field has to fill |
| 2 | `FIELD_COL` | DOUBLE | NOT NULL |  | Column where field starts |
| 3 | `FIELD_ROW` | DOUBLE | NOT NULL |  | Row where field starts |
| 4 | `FORM_FIELD_ID` | DOUBLE | NOT NULL | PK | Unique Id used for different types of fields for a specific forms |
| 5 | `OSM_FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Type of Field used by the Form |
| 6 | `OSM_FORM_ID` | DOUBLE | NOT NULL |  | Unique Form Id form OSM_FORM table |
| 7 | `TEXT` | VARCHAR(100) |  |  | Form specific text entered by user |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_GROUP_NBR` | DOUBLE | NOT NULL |  | This field identifies the set of fields on the form to which the field belongs and the position of that set of fields on the form. |
| 14 | `VALUE_SEQ_NBR` | DOUBLE | NOT NULL |  | This field identifies the sequence that values will be filled within a group and the fields with the same sequence that will share a value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OSM_FORM_CLIENT_VALUES](OSM_FORM_CLIENT_VALUES.md) | `FORM_FIELD_ID` |
| [OSM_FORM_GROUP_VALUES](OSM_FORM_GROUP_VALUES.md) | `FORM_FIELD_ID` |

