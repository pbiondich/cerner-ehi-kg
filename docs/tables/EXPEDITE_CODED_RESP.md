# EXPEDITE_CODED_RESP

> Used to trigger an expedite chart by a coded response for a task assay.

**Description:** EXPEDITE CODED RESP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODED_RESPONSE_CD` | DOUBLE | NOT NULL |  | Micro code_values for coded responses. Uses code set 1021 for organisms and 1022 for the other responses. |
| 2 | `EXPEDITE_TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | Part of primary key |
| 3 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | coded resp |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPEDITE_TRIGGER_ID` | [EXPEDITE_TRIGGER](EXPEDITE_TRIGGER.md) | `EXPEDITE_TRIGGER_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

