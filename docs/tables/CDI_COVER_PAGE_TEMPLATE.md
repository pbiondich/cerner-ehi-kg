# CDI_COVER_PAGE_TEMPLATE

> Stores templates used to generate cover pages used when faxing CPDI documents outbound.

**Description:** CPDI Cover Page Template  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_COVER_PAGE_TEMPLATE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_COVER_PAGE_TEMPLATE table. |
| 2 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the LONG_TEXT table row containing the contents of the template. |
| 3 | `TEMPLATE_NAME` | VARCHAR(100) | NOT NULL |  | The name of the template. |
| 4 | `TEMPLATE_NAME_KEY` | VARCHAR(100) | NOT NULL |  | The name key of the template. |
| 5 | `TEMPLATE_NAME_KEY_A_NLS` | VARCHAR(400) | NOT NULL |  | Stores the corresponding non-english ACCENTED character set values for the TEMPLATE_NAME_KEY column. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

