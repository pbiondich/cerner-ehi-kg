# LH_CNT_IC_PATIENT_MDRO_RSK

> This table stores patient's MDRO risk information

**Description:** LH CNT IC PATIENT MDRO RSK  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATEGORY_NAME` | VARCHAR(150) |  |  | The MDRO category name |
| 3 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code for this mdro |
| 4 | `LH_CNT_IC_PATIENT_MDRO_RSK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_MDRO_RISK table. |
| 5 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to lh_cnt_ic_patient_pop |
| 6 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | 1=NEW, 2=HIST, 3=RECURRING |
| 7 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | 1 = NHSN, 2 = OTHER |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |

