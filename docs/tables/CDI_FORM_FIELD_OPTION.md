# CDI_FORM_FIELD_OPTION

> Associate text or code value options to form fields as configured in CDIConfig.

**Description:** CDI Form Field Option  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_FORM_FIELD_ID` | DOUBLE |  | FK→ | Identifies a row on the cdi_form_field table to which this option row is associated. |
| 2 | `CDI_FORM_FIELD_OPTION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the cdi_form_field_option table.; |
| 3 | `OPTION_TYPE_TFLAG` | VARCHAR(10) |  |  | Indicates the type of the text value (allowable values: "TEXT", "CODEVALUE"). |
| 4 | `OPTION_VALUE_TEXT` | VARCHAR(150) |  |  | A text value for an option (i.e. dropdown text selection, code set & code value pair). |
| 5 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_FORM_FIELD_ID` | [CDI_FORM_FIELD](CDI_FORM_FIELD.md) | `CDI_FORM_FIELD_ID` |

