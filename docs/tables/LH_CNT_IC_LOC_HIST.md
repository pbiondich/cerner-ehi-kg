# LH_CNT_IC_LOC_HIST

> patient locations based on a specific time.

**Description:** Lighthouse Content Infection Control Location History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BED_LOC_CD` | DOUBLE | NOT NULL | FK→ | Physical Bed Location of the patient at the location type time. |
| 2 | `BUILD_LOC_CD` | DOUBLE | NOT NULL | FK→ | Physical building location of the patient at the location type time. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter being reported on. |
| 4 | `FAC_LOC_CD` | DOUBLE | NOT NULL | FK→ | The facility of the patient at the location type time. |
| 5 | `LH_CNT_IC_LOC_HIST_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the LH_CNT_IC_LOC_HIST table. |
| 6 | `LOC_TYPE_FLAG` | DOUBLE | NOT NULL |  | The location type of the encounter being reported on. (1 = Admit, 2 = Order, 3 = Collect. |
| 7 | `NU_LOC_CD` | DOUBLE | NOT NULL | FK→ | The Nursing Unit of the patient at the location type time. |
| 8 | `ROOM_LOC_CD` | DOUBLE | NOT NULL | FK→ | The room location of the patient at the location type time. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BED_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `BUILD_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FAC_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `NU_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ROOM_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

