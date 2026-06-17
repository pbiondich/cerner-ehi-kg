# PULSE_GEN_EPISODE

> Contains information about an atypical heart rhythm event that a pulse generator device has recorded.

**Description:** Pulse Generator Episode  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `A_INT_DET_NBR` | DOUBLE |  |  | The atrial interval at the time of detection |
| 2 | `A_INT_TERM_NBR` | DOUBLE |  |  | The atrial interval at the time of termination |
| 3 | `DETAILS_TXT` | VARCHAR(100) |  |  | A text describing details about the detection and therapy delivered |
| 4 | `DETECTION_DT_TM` | DATETIME |  |  | The detection date and time of the episode |
| 5 | `DOC_LEN_NBR` | DOUBLE |  |  | The number of pages for this session document |
| 6 | `DOC_UID` | VARCHAR(50) | NOT NULL |  | The UID for a document associated with this episode |
| 7 | `DURATION_VALUE` | DOUBLE | NOT NULL |  | The duration of the episode in seconds |
| 8 | `EPISODE_IDENT` | VARCHAR(100) |  |  | The unique identifier for the episode |
| 9 | `INDUCED_CD` | DOUBLE | NOT NULL |  | The indication of whether the episode has been induced or not |
| 10 | `PULSE_GEN_EPISODE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `PULSE_GEN_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator associated with this episode |
| 12 | `THERAPY_RESULT_CD` | DOUBLE | NOT NULL |  | The indicator of therapy success |
| 13 | `TYPE_CD` | DOUBLE | NOT NULL |  | The generic type of the episode being reported |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VENDOR_TYPE_CD` | DOUBLE | NOT NULL |  | The vendor type of the episode being reported |
| 20 | `V_INT_DET_NBR` | DOUBLE |  |  | The ventricular interval at the time of detection |
| 21 | `V_INT_TERM_NBR` | DOUBLE |  |  | The ventricular interval at the time of termination |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_ID` | [PULSE_GEN](PULSE_GEN.md) | `PULSE_GEN_ID` |

