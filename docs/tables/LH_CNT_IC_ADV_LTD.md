# LH_CNT_IC_ADV_LTD

> This table will be used to store results of Lines, Tubes, Drains (LTD) for our advisor.

**Description:** LH_CNT_IC_ADV_LTD  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CE_DYNAMIC_LABEL_ID` | DOUBLE | NOT NULL | FK→ | The label_id of the dynamic label that this LTD is associated with. (From CE_DYNAMIC_LABEL table) |
| 3 | `DISCONTINUE_DT_TM` | DATETIME |  |  | This field will be used to store the discontinue date time of the LTD. If the line has not yet been discontinued, the value in this column will be NULL. |
| 4 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to EKS_ADVSR_EVENT table. This will allow us to identify the unique instance of an advisor that this row belongs to. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ENCOUNTER table. Stores the encounter that the LTD was attached to. |
| 6 | `INSERT_DT_TM` | DATETIME |  |  | This field will be used to store the insertion date time of the LTD. |
| 7 | `LH_CNT_IC_ADV_LTD_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_ADV_LTD table. |
| 8 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | This field is the patient location with a location type of bed at the time this LTD was placed. CODE SET: 220 |
| 9 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the facility location at which this LTD was placed. CODE SET: 220 |
| 10 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the nurse unit location at which this LTD was placed. CODE SET: 220 |
| 11 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | This field is the patient location with a location type of room at the time this LTD was placed. CODE SET: 220 |
| 12 | `LTD_CATEGORY_NAME` | VARCHAR(255) |  |  | This field indicates which category of LTD this row belongs to. Examples include: Central, Arterial, Artificial Airway, et al. |
| 13 | `LTD_DESCRIPTION` | VARCHAR(1000) |  |  | This field indicates the general description of the LTD. Factors such as the size of the LTD usually go here. |
| 14 | `LTD_LOCATION` | VARCHAR(100) |  |  | This field indicates the location of the LTD. Generally, factors such as the laterality and site usually are used for this column. |
| 15 | `LTD_TYPE` | VARCHAR(255) |  |  | This field indicates the type of LTD that this row belongs to. Examples include Non-Tunneled for Central Line, Permanent for Central Line, Indwelling/Continuous for Urinary Catheter, et al. |
| 16 | `PRESENT_ON_ADMISSION_IND` | DOUBLE |  |  | This field will be set to 1 if the LTD was present on admission, 0 otherwise. |
| 17 | `TOTAL_DURATION_DAYS` | DOUBLE |  |  | This field indicates the total duration of the LTD. This is calculated via the time difference between the insertion date time and discontinued date time. If the line has not yet been discontinued, then total duration will be calculated from the time difference between insertion date time and current date time |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_DYNAMIC_LABEL_ID` | [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `CE_DYNAMIC_LABEL_ID` |
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

