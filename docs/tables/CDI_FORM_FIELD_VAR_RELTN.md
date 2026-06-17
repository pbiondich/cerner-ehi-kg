# CDI_FORM_FIELD_VAR_RELTN

> A row in this table represents a link from a patient eSignature form to a Millennium variable (eg, a registration UDF field or health plan relationship field).

**Description:** CDI_FORM_FIELD_VAR_RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_FORM_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The ID of the form field this variable is linked to. A foreign key to the cdi_form_field table. |
| 2 | `CDI_FORM_FIELD_VAR_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_FORM_FIELD_VAR_RELTN table. |
| 3 | `FIELD_STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the status this field must have before the linked variable is updated. 0 - Not set (unchecked or unsigned), 1 - Set (checked or signed), 2- Declined, 3 - Embedded. |
| 4 | `LINKED_VALUE_CD` | DOUBLE | NOT NULL |  | Indicates the data variable that will be set if this field is updated. The code set will vary depending on what is selected in linked_variable_cd. |
| 5 | `LINKED_VALUE_NBR` | DOUBLE | NOT NULL |  | Indicates the numeric value that will be stored if this field updated. |
| 6 | `LINKED_VALUE_TEXT` | VARCHAR(150) |  |  | Indicates the text value that will be stored if this field is updated. |
| 7 | `LINKED_VARIABLE_CD` | DOUBLE | NOT NULL |  | Indicates the code value that will be stored if this field is updated. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_FORM_FIELD_ID` | [CDI_FORM_FIELD](CDI_FORM_FIELD.md) | `CDI_FORM_FIELD_ID` |

