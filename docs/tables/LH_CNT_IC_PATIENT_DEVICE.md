# LH_CNT_IC_PATIENT_DEVICE

> This table stores information about medical devices hooked up to the patient

**Description:** LH_CNT_IC_PATIENT_DEVICE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CE_DYNAMIC_LABEL_ID` | DOUBLE | NOT NULL | FK→ | Unique, generated primary key for ce_dynamic_label table. |
| 3 | `DISCONTINUE_DT_TM` | DATETIME |  |  | The date/time the LTD was discontinued. |
| 4 | `ESTIMATED_DATE_IND` | DOUBLE | NOT NULL |  | Indicator to determine if the inserted date/time is estimated or not. 0=not estimated, 1 = estimated |
| 5 | `LH_CNT_IC_PATIENT_DEVICE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_DEVICE table. |
| 6 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to lh_cnt_ic_patient_pop. |
| 7 | `LINE_DISPLAY` | VARCHAR(255) |  |  | The line inserted into the patient. Ex: Artificial Airway, Chest Tube #1, Central Line IV |
| 8 | `LINE_INSERTED_DT_TM` | DATETIME |  |  | The date/time the line was inserted |
| 9 | `LINE_TYPE_DISPLAY` | VARCHAR(255) |  |  | The type of line inserted into the patient. Ex: Tunneled, over the needle |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_DYNAMIC_LABEL_ID` | [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `CE_DYNAMIC_LABEL_ID` |
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |

