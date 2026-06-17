# EKS_TEMPLATE_DOC

> Text help for template goals and usage

**Description:** Textual help file for template goals and usage.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_SEQ` | DOUBLE | NOT NULL |  | If the number of records required to represent the help text ( each record is limited to 2000 chars) is > 1 then this seq number is used to indicate the sequence of the records. |
| 2 | `TEMPLATE_DOC` | VARCHAR(2000) |  |  | The text of the template documentation. If the total text is over 2000 characters, the text will be broken up into multiple records with the data_seq field used as a sequence number. |
| 3 | `TEMPLATE_NAME` | CHAR(30) | NOT NULL |  | The template name that this doc applies to |
| 4 | `TEMPLATE_TYPE` | CHAR(1) |  |  | The template's type E)voke, L)ogic, or A)ction. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

