# BR_INSTR_ORG_RELTN

> instruments for each organization

**Description:** BEDROCK INTSTRUMENT ORGANIZATION RELATIONSHIP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_MEAN` | VARCHAR(12) |  |  | the activity type meaning indicating where/how the instrument is used (i.e. chemistry) |
| 2 | `BI_IND` | DOUBLE | NOT NULL |  | indicates if instrument is bi-directional |
| 3 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 4 | `BR_INSTR_ID` | DOUBLE | NOT NULL |  | Identifies the instrument being associated to an org - from br_instr table |
| 5 | `BR_INSTR_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | BEDROCK INSTR ORGANIZATION RELATION IDENTIFIER value |
| 6 | `HQ_IND` | DOUBLE | NOT NULL |  | indicates if instrument is hq |
| 7 | `INTERFACE_IND` | DOUBLE | NOT NULL |  | indicates if there is an interface to this instrument or not |
| 8 | `MANUFACTURER` | VARCHAR(100) |  |  | manufacturer of the instrument - from the br_instr table |
| 9 | `MODEL` | VARCHAR(100) |  |  | model of the instrument - from the br_instr table |
| 10 | `MODEL_DISP` | VARCHAR(100) |  |  | the display value of the model of instrument |
| 11 | `MULTIPLEXOR_IND` | DOUBLE | NOT NULL |  | indicates if the instrument is a multiplexor |
| 12 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | the id of the organization that the instrument is associated with |
| 13 | `POC_IND` | DOUBLE | NOT NULL |  | indicates if instrument is a point-of-care instrument |
| 14 | `ROBOTICS_IND` | DOUBLE | NOT NULL |  | indicates if the instrument has robotics |
| 15 | `TYPE` | VARCHAR(50) |  |  | type of instrument - from the br_instr table |
| 16 | `UNI_IND` | DOUBLE | NOT NULL |  | indicates instrument is uni-directional |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

