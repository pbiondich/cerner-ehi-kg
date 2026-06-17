# CDI_FORM_FIELD_ACTIVITY

> This table tracks the status of each field on an instance of a CDI_FORM.

**Description:** CDI_FORM_FIELD_ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_FORM_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the CDI_FORM_ACTIVITY table. |
| 2 | `CDI_FORM_FIELD_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_FORM_FIELD_ACTIVITY table. |
| 3 | `CDI_FORM_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the CDI_FORM_FIELD table. |
| 4 | `FIELD_STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of the form field. 0=Complete 1=Pending 2=Declined |
| 5 | `FIELD_VALUE_TEXT` | VARCHAR(150) |  |  | This will support capturing the (first 150 characters of) text values entered by patients on text fields for patient forms. Capturing the text value will allow reports to be written that display the values entered by patients (without displaying the actual document itself). |
| 6 | `PAGE_NBR` | DOUBLE | NOT NULL |  | The page number that the field appears on. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_FORM_ACTIVITY_ID` | [CDI_FORM_ACTIVITY](CDI_FORM_ACTIVITY.md) | `CDI_FORM_ACTIVITY_ID` |
| `CDI_FORM_FIELD_ID` | [CDI_FORM_FIELD](CDI_FORM_FIELD.md) | `CDI_FORM_FIELD_ID` |

