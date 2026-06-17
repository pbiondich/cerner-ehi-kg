# LH_CNT_LTD_DATA_DETAIL

> Child table to the LH_CNT_LTD_DATA summary table that stores details associated with Lines, Tubes, Drains.

**Description:** LH_CNT_LTD_DATA_DETAIL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DETAIL_TYPE_FLAG` | DOUBLE |  |  | The type of detail stored by this row. (Laterality, Description, Vent Mode, etc.) |
| 3 | `EVENT_END_DT_TM` | DATETIME |  |  | The event_end_dt_tm of the detail taken from CLINICAL_EVENT. |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event_id for the detail taken from CLINICAL_EVENT. |
| 5 | `LH_CNT_LTD_DATA_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_LTD_DATA_DETAIL table. |
| 6 | `LH_CNT_LTD_DATA_ID` | DOUBLE | NOT NULL | FK→ | Foreign key id link to the parent row on LH_CNT_LTD_DATA for the associated detail. |
| 7 | `NOMEN_ID` | DOUBLE | NOT NULL | FK→ | The nomenclature_id for the detail associated to the event_id taken from CLINICAL_EVENT(if found). |
| 8 | `RESULT_VAL` | VARCHAR(255) |  |  | The result value for the detail taken from CLINICAL_EVENT. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_LTD_DATA_ID` | [LH_CNT_LTD_DATA](LH_CNT_LTD_DATA.md) | `LH_CNT_LTD_DATA_ID` |
| `NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

