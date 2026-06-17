# RC_F_MTH_CODING_ACT_SMRY

> This table will store monthly summarization of coding activity by coding personnel.

**Description:** ProFit Revenue Cycle Warehouse  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_YEAR` | DOUBLE | NOT NULL |  | Contains the year in which the activity took place. |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time the record was first loaded into the table. |
| 3 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time the record was last loaded into the table. |
| 4 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Represents the transaction's logical domain. |
| 5 | `RC_D_CODING_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the coding activity related to this fact row. |
| 6 | `RC_D_DRG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the DRG associated tot the encounter related to this coding activity. |
| 7 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter associated to this coding |
| 8 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 9 | `RC_D_PRI_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Number that uniquely identifies the primary financial class related to this fact row. |
| 10 | `RC_D_PRI_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the primary health plan related to this fact row. |
| 11 | `RC_F_MTH_CODING_ACT_SMRY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_F_MTH_CODING_ACT_SMRY table. |
| 12 | `SHR_D_CODING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the coding personnel related to this coding activity. |
| 13 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies location information related to this fact row. |
| 14 | `SHR_D_MONTH_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the month related to this fact row. |
| 15 | `TOTAL_ACTIONS_COUNT` | DOUBLE | NOT NULL |  | The total actions count per coding personnel. |
| 16 | `TOTAL_ENCOUNTER_COUNT` | DOUBLE | NOT NULL |  | The total number of encounters associated to this coding activity. |
| 17 | `TOTAL_FE_BALANCE_AMT` | DOUBLE | NOT NULL |  | The total of the financial encounter balance amount for the patient who had the coding activity. |
| 18 | `TOTAL_LENGTH_OF_STAY` | DOUBLE | NOT NULL |  | The total number of midnights the patient stays in the hospital, from admission to either discharge or coding activity date, which ever occurs first. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_D_CODING_ACTION_ID` | [RC_D_CODING_ACTION](RC_D_CODING_ACTION.md) | `RC_D_CODING_ACTION_ID` |
| `RC_D_DRG_ID` | [RC_D_DRG](RC_D_DRG.md) | `RC_D_DRG_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_PRI_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_PRI_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `SHR_D_CODING_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |

