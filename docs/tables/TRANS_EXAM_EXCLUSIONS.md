# TRANS_EXAM_EXCLUSIONS

> The Trans_Exam_Exclusion table contains exams that should be excluded whenever a batch folder transfer is executed.

**Description:** Transfer Exam Exclusions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The Catalog_Cd is a foreign key to the Order_Catalog table. It uniquely identifies the exam that is to be excluded from the transfer pull list. |
| 2 | `TRANS_RULE_ID` | DOUBLE | NOT NULL | FK→ | The trans_rule_id serves as a foreign key to the rad_fold_trans_rule table. It uniquely identifies the transfer rule that the exam exclusions are a part of. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `TRANS_RULE_ID` | [RAD_FOLD_TRANS_RULE](RAD_FOLD_TRANS_RULE.md) | `TRANS_RULE_ID` |

