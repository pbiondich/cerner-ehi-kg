# RXS_LOCATOR_ENCNTR

> Stores a locator's relation to a patient's encounter.

**Description:** RxStation Locator Encounter  
**Table type:** ACTIVITY  
**Primary key:** `RXS_LOCATOR_ENCNTR_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLUSTER_CD` | DOUBLE | NOT NULL | FK→ | The cluster that this locator is part of. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The patient's encounter that is supplied through this locator. |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Identifies an RxStation device. |
| 4 | `LOCATOR_CD` | DOUBLE | NOT NULL | FK→ | The bin location which is tied to this encounter. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person whose encounter information is linked to this location. |
| 6 | `RXS_LOCATOR_ENCNTR_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RXS_LOCATOR_ENCNTR table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLUSTER_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATOR_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RXS_LOC_ENCNTR_INVENTORY](RXS_LOC_ENCNTR_INVENTORY.md) | `RXS_LOCATOR_ENCNTR_ID` |

