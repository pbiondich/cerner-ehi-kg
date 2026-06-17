# SI_UNMTCHD_PRSN_ALIAS

> This table will store the aliases related to an inbound message if it can't be matched to an existing person.

**Description:** System Integration Unmatched Person Alias  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_NAME` | VARCHAR(200) | NOT NULL |  | Primary Alias from message |
| 2 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias Pool Code from Message |
| 3 | `ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Alias type code from message |
| 4 | `SI_UNMTCHD_PRSN_ALIAS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY IDENTIFIER |
| 5 | `SI_UNMTCHD_PRSN_QUE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to si_unmatched_person_qure |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_UNMTCHD_PRSN_QUE_ID` | [SI_UNMTCHD_PRSN_QUE](SI_UNMTCHD_PRSN_QUE.md) | `SI_UNMTCHD_PRSN_QUE_ID` |

