# CDI_TRANS_MOD_DETAIL

> This table tracks details for CPDI image modifications.

**Description:** cdi rans mod detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | Action sequence column |
| 2 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Description of the modification. (1=rotate, 2=delete, 3=add, 4=reorder, 5=cut, 6=copy, 7=annotate, 8=rollback, 9=add version, 10=ocr (optical character recognition), 11=modify text), 12 - resume checkout. |
| 3 | `CDI_TRANS_LOG_ID` | DOUBLE | NOT NULL | FK→ | ID of the parent cdi_trans_log row. |
| 4 | `CDI_TRANS_MOD_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique ID for each image modification detail. |
| 5 | `END_PAGE` | DOUBLE | NOT NULL |  | Last page of the document affected. |
| 6 | `POSITION` | DOUBLE | NOT NULL |  | New position of the pages in the document for reorder action. |
| 7 | `START_PAGE` | DOUBLE | NOT NULL |  | First page of the document affected. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_TRANS_LOG_ID` | [CDI_TRANS_LOG](CDI_TRANS_LOG.md) | `CDI_TRANS_LOG_ID` |

