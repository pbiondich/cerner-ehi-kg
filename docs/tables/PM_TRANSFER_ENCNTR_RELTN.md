# PM_TRANSFER_ENCNTR_RELTN

> This table is used to record the transfer of an encounter prsnl reltation from one prsnl to another. This information can then be used to undo the transfer.

**Description:** Encounter/transfer relationship.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 4 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | Encounter personnel relationship code identifies the type of relationship between the prsnl and the encounter. (For Example: Attending Physician, Admitting Physician, etc.) |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PM_TRANSFER_ENCNTR_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_transfer_encntr_reltn table. It is an internal system assigned number. |
| 7 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the prsnl table. It is an internal system assigned number. |
| 8 | `TRANSFER_PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the prsnl table. It is an internal system assigned number. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRANSFER_PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

