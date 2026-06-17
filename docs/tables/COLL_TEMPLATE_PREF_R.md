# COLL_TEMPLATE_PREF_R

> Stores the relationship preference for Collection Templates.

**Description:** COLL TEMPLATE PREF R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_RELATION_CD` | DOUBLE | NOT NULL |  | The child relation code for the parent. |
| 2 | `COLL_TEMPLATE_CD` | DOUBLE | NOT NULL | FK→ | The collection template code value. |
| 3 | `MODE_FLAG` | DOUBLE | NOT NULL |  | The mode for this relationship preference. 1 - By location 2 - By list 3 - By Accession 4 - By Patient |
| 4 | `PARENT_RELATION_CD` | DOUBLE | NOT NULL |  | The parent code value for this relationship. |
| 5 | `RELATION` | DOUBLE | NOT NULL |  | The relationship type of this preference. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLL_TEMPLATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

