# MM_XFI_CNTRCT_PRICE_ADJ

> Table used to store relationships between contracts and price adjustments. Data is moved from this table to MM_CNTRCT_PRICE_ADJ.

**Description:** MM XFI CNTRCT PRICE ADJ  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Adjustment action flag |
| 2 | `ADJUSTMENT` | DOUBLE |  |  | adjustment |
| 3 | `ADJ_CLASS_NODE` | VARCHAR(60) |  |  | Adjustment class node |
| 4 | `ADJ_CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Adjustment class node key |
| 5 | `ADJ_METRIC` | VARCHAR(60) |  |  | Adjustment metric |
| 6 | `ADJ_METRIC_CD` | DOUBLE | NOT NULL |  | Adjustment metric code value |
| 7 | `ADJ_TYPE` | VARCHAR(60) |  |  | Adjustment type |
| 8 | `ADJ_TYPE_CD` | DOUBLE | NOT NULL |  | Adjustment type code value |
| 9 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code value |
| 10 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 11 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time the note was created. |
| 12 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 13 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 14 | `PRICE_ADJ_ID` | DOUBLE | NOT NULL | FK→ | price adjustment identifier |
| 15 | `PROCESS_FLAG` | DOUBLE |  |  | process flag |
| 16 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Primary key |
| 17 | `TRANS_PARENT_ID` | DOUBLE | NOT NULL | FK→ | transaction parent identifier |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADJ_CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `PRICE_ADJ_ID` | [MM_CNTRCT_PRICE_ADJ](MM_CNTRCT_PRICE_ADJ.md) | `PRICE_ADJ_ID` |
| `TRANS_PARENT_ID` | [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `TRANSACTION_ID` |

