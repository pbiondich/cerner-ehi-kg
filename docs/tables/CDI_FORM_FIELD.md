# CDI_FORM_FIELD

> A row in this table represents an interactive field on a CPDI interactive form.

**Description:** CDI Form Field  
**Table type:** REFERENCE  
**Primary key:** `CDI_FORM_FIELD_ID`  
**Columns:** 29  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_FORM_FIELD_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated number. |
| 2 | `CDI_FORM_ID` | DOUBLE | NOT NULL | FK→ | The ID of the form the field appears on. A foreign key to the CDI_FORM table. |
| 3 | `FIELD_DESCRIPTION` | VARCHAR(500) | NOT NULL |  | Description of the form field. |
| 4 | `FIELD_HEIGHT` | DOUBLE | NOT NULL |  | The height of the field. |
| 5 | `FIELD_NAME` | VARCHAR(40) | NOT NULL |  | The name of the field. Used primarily by RDDS to match rows across domains. |
| 6 | `FIELD_ROTATION_VALUE` | DOUBLE | NOT NULL |  | The orientation of the field, in degrees of rotation counterclockwise. |
| 7 | `FIELD_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of interactive field. 0 - Signature, 1 - Checkbox, 2 - Text, 3 - Group, 4 - Required Signature |
| 8 | `FIELD_WIDTH` | DOUBLE | NOT NULL |  | The width of the field. |
| 9 | `FONT_FAMILY_FLAG` | DOUBLE | NOT NULL |  | Font family to be used when displaying a text field.0 = sans-serif (e.g. Arial)1 = serif (e.g. Times)2 = monospace (e.g. Courier)256 = sans-serif italic 257 = serif italic 258 = monospace italic 512 = sans-serif bold 513 = serif bold 514 = monospace bold 768 = sans-serif bold italic 769 = serif bold italic 770 = monospace bold italic 2048 = bar code 128 2049 = bar code 3 of 9 extended 3072 = bar code PDF 417 3073 = bar code datamatrix |
| 10 | `FONT_SIZE_NBR` | DOUBLE | NOT NULL |  | Font size to be used when displaying a text field. |
| 11 | `FORM_COMPLETION_FLAG` | DOUBLE | NOT NULL |  | Identifies how completion of this field affects completion of the entire form. 0 - No effect, 1- Declined if not set, 2 - Declined if set. |
| 12 | `LAST_PAGE_NBR` | DOUBLE | NOT NULL |  | The last page number that the field appears on. |
| 13 | `LINKED_VALUE_CD` | DOUBLE | NOT NULL |  | Indicates the code value that will be stored if this field is set. The code set will vary depending on what is selected in linked_variable_cd. OBSOLETE COLUMN |
| 14 | `LINKED_VALUE_NBR` | DOUBLE | NOT NULL |  | Indicates the numeric value that will be stored if this field is set. OBSOLETE COLUMN |
| 15 | `LINKED_VALUE_TEXT` | VARCHAR(150) |  |  | Indicates the text value that will be stored if this field is set. OBSOLETE COLUMN |
| 16 | `LINKED_VARIABLE_CD` | DOUBLE | NOT NULL |  | Identifies the data variable that will be set if this field is set. OBSOLETE COLUMN |
| 17 | `OPTIONS_SOURCE_TFLAG` | VARCHAR(10) |  |  | Indicates the source of the options for a select field (allowable values: "CUSTOM", "ORDERS"). |
| 18 | `PAGE_NBR` | DOUBLE | NOT NULL |  | The first page number that the field appears on. |
| 19 | `PARENT_FORM_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Indicates that this field is associated to a parent form field. |
| 20 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates that this field is required. |
| 21 | `TEXT_COLOR_NBR` | DOUBLE | NOT NULL |  | RGB color to be used when displaying a text field. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VALUE_FORMAT_TEXT` | VARCHAR(150) |  |  | Indicates the format for text fields. |
| 28 | `X_COORD` | DOUBLE | NOT NULL |  | Position x coordinate that the field appears at. |
| 29 | `Y_COORD` | DOUBLE | NOT NULL |  | Position y coordinate that the field appears at. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_FORM_ID` | [CDI_FORM](CDI_FORM.md) | `CDI_FORM_ID` |
| `PARENT_FORM_FIELD_ID` | [CDI_FORM_FIELD](CDI_FORM_FIELD.md) | `CDI_FORM_FIELD_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CDI_FORM_FIELD](CDI_FORM_FIELD.md) | `PARENT_FORM_FIELD_ID` |
| [CDI_FORM_FIELD_ACTIVITY](CDI_FORM_FIELD_ACTIVITY.md) | `CDI_FORM_FIELD_ID` |
| [CDI_FORM_FIELD_OPTION](CDI_FORM_FIELD_OPTION.md) | `CDI_FORM_FIELD_ID` |
| [CDI_FORM_FIELD_VAR_RELTN](CDI_FORM_FIELD_VAR_RELTN.md) | `CDI_FORM_FIELD_ID` |

