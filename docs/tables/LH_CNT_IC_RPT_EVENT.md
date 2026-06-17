# LH_CNT_IC_RPT_EVENT

> This table will store Lighthouse Content Report data.

**Description:** LH_CNT_IC_RPT_EVENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CE_DYNAMIC_LABEL_ID` | DOUBLE | NOT NULL | FK→ | The dynamic label is a grouper id for the dynamic groups documented on the clinical event table. |
| 3 | `DISCONTINUE_DT_TM` | DATETIME |  |  | The date and time the line was removed. From the clinical event tables, event_end_dt_tm. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter id on lh_cnt_ic_rpt_event relates to the encounter table. |
| 5 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event cd on the lh_cnt_ic_rpt_event relates to the clinical event documented on the patient. |
| 6 | `EVENT_DT_TM` | DATETIME |  |  | The event date time is the date and time the event was documented from the clinical event table |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event id on the lh_cnt_ic_rpt_event relates to the clinical event table. |
| 8 | `EVENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The event type flag is an identifier for the type of event.1=Contact Person,2=Contact Method,3=Contact Agency,4 =Contact Date,5=Condition,6=Device Type,7=Device Location,8=Device Line Care,9=Device Vent Mode,10=Blood Pressure,11=Device Description,12=Device Laterality,13=Device Insert/Start,14 = Device,Discontinue/End,15=Birthweight,16=Present on Admission,20=Central line,21=Arterial line,22=PA line,23=LA line,24=IA Balloon Pump,25=Peripheral line,26=Chest Tube,27=Gastric Tube,28-35.... |
| 9 | `INSERT_DT_TM` | DATETIME |  |  | The date and time the line was inserted. From the clinical event tables, event_end_dt_tm. |
| 10 | `LH_CNT_IC_RPT_EVENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_RPT_EVENT table. |
| 11 | `RESULT_DISPLAY` | VARCHAR(255) |  |  | The result display is the text version of the results documented on events on the clinical event table. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_DYNAMIC_LABEL_ID` | [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `CE_DYNAMIC_LABEL_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

