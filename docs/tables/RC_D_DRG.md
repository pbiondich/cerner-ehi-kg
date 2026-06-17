# RC_D_DRG

> Contains infrormation related to the diagnosis related group.

**Description:** Revenue Cycle Dimension Diagnosis Related Group  
**Table type:** ACTIVITY  
**Primary key:** `RC_D_DRG_ID`  
**Columns:** 17  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DRG_CODE_TXT` | VARCHAR(50) | NOT NULL |  | Contains the code that represents diagnosis. |
| 4 | `DRG_DESCRIPTION` | VARCHAR(200) | NOT NULL |  | The description of a drg as defined by the client. |
| 5 | `DRG_WEIGHT` | DOUBLE | NOT NULL |  | Stores the DRG weight for groupers |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 9 | `MILL_DRG_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related DRG from the Millennium nomenclature table. |
| 10 | `RC_D_DRG_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a DRG that has ben posted to the clinical encounter. |
| 11 | `SOURCE_VOCABULARY_CODE` | DOUBLE | NOT NULL |  | Contains the source vocabulary code value. |
| 12 | `SOURCE_VOCABULARY_DESC` | VARCHAR(100) | NOT NULL |  | Contains the source vocabulary code description. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (8)

| From table | Column |
|------------|--------|
| [RC_F_CASE_MIX](RC_F_CASE_MIX.md) | `MS_DRG_ID` |
| [RC_F_CASE_MIX](RC_F_CASE_MIX.md) | `RC_D_PRI_DRG_ID` |
| [RC_F_CODING_ACTIVITY](RC_F_CODING_ACTIVITY.md) | `RC_D_DRG_ID` |
| [RC_F_DAILY_CENSUS](RC_F_DAILY_CENSUS.md) | `RC_D_DRG_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_D_DRG_ID` |
| [RC_F_DLY_CODING_ACT_SMRY](RC_F_DLY_CODING_ACT_SMRY.md) | `RC_D_DRG_ID` |
| [RC_F_MTH_CODING_ACT_SMRY](RC_F_MTH_CODING_ACT_SMRY.md) | `RC_D_DRG_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_PRI_DRG_ID` |

