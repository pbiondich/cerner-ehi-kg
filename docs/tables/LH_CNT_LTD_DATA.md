# LH_CNT_LTD_DATA

> Summary table for all dynamic group Lines, Tubes, and Drains.

**Description:** LH_CNT_LTD_DATA  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_LTD_DATA_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CE_DYNAMIC_LABEL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to CE_DYNAMIC_LABEL for the dynamic group the ltd was documented on. |
| 3 | `DISC_DT_TM` | DATETIME |  |  | Discontinue date and time for the ltd. |
| 4 | `INSERT_DT_TM` | DATETIME |  |  | Insertion date and time for the ltd. |
| 5 | `INSERT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ENCOUNTER table for the encounter in which the line was inserted. |
| 6 | `INSERT_LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | Bed in which the person was located when the ltd was inserted. |
| 7 | `INSERT_LOC_FAC_CD` | DOUBLE | NOT NULL | FK→ | Facility in which the person was located when the ltd was inserted |
| 8 | `INSERT_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Nurse unit in which the person was located when the ltd was inserted. |
| 9 | `INSERT_LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | Room in which the person was located when the ltd was inserted. |
| 10 | `LH_CNT_LTD_DATA_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CNT_LTD_DATA table. |
| 11 | `LTD_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the ltd type. (Central line, urinary catheter, etc.) |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to PERSON table for whom the line belongs. |
| 13 | `POA_DT_TM` | DATETIME |  |  | Date and time of the initial present on admission documentation. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VESSEL_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the vessel type. (Umbilical, great vessel, etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_DYNAMIC_LABEL_ID` | [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `CE_DYNAMIC_LABEL_ID` |
| `INSERT_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `INSERT_LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `INSERT_LOC_FAC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `INSERT_LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `INSERT_LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LH_CNT_LTD_DATA_DETAIL](LH_CNT_LTD_DATA_DETAIL.md) | `LH_CNT_LTD_DATA_ID` |

