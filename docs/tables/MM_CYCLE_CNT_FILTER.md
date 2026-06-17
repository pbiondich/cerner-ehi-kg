# MM_CYCLE_CNT_FILTER

> Stores some of the parameters needed to create a cycle count.

**Description:** Cycle Count Filter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABC_CLASS_CD` | DOUBLE | NOT NULL |  | Denotes the ABC classification of the items on this cycle count. |
| 2 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Denotes the Class node of the items on this cycle count. |
| 3 | `FILTER_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of parameter this row pertains to. |
| 4 | `MM_CYCLE_CNT_FILTER_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MM_CYCLE_CNT_FILTER table. |
| 5 | `MM_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | %applyes% |
| 6 | `SORT_METHOD_TXT` | VARCHAR(50) | NOT NULL |  | Denotes how the items are going to be sorted. |
| 7 | `SORT_SEQ` | DOUBLE | NOT NULL |  | The sequence to apply when sorting by sort_txt. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `MM_TEMPLATE_ID` | [MM_TEMPLATE](MM_TEMPLATE.md) | `MM_TEMPLATE_ID` |

