# LH_CNT_IC_CLUST_ANALYSIS

> This table will contain data related to cluster analysis. A cluster analysis is determining when there are multiple instances of a client specified organism over a client defined timeframe. In other words, they may want to be alerted if they have three e-coli results in seven days.

**Description:** lh_cnt_ic_clust_analysis  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIT_DT_TM` | DATETIME | NOT NULL |  | The admit date is flexed based on the client for interfaced results. Can be the arrive_dt_tm or the reg_dt_tm from the encounter table. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CLINICAL_EVENT_ID` | DOUBLE | NOT NULL |  | Unique key from the clinical_event table. This is passed in from a Discern Rule to begin the evaluation. |
| 4 | `COLLECT_DT_TM` | DATETIME | NOT NULL |  | Date and time the specimen was collected used for the timeframe parameters in determining the cluster or outbreak. From the CE_SPECIMEN_COLL table. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Unique key from the Encounter table. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EVENT_CD` | DOUBLE | NOT NULL |  | Code value for the event_codes from clinical event |
| 8 | `EVENT_ID` | DOUBLE | NOT NULL |  | Non-unique field from the clinical_event table. Used in conjunction with valid_until_dt_tm from child tables to form unique indexes. |
| 9 | `FIN` | VARCHAR(100) |  |  | From the alias field on the encntr_alias table. Needed for reporting. |
| 10 | `LH_CNT_IC_CLUST_ANALYSIS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the lh_cnt_ic_clust_analysis table. |
| 11 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | Identifies the bed where the encounter took place. Needed for reporting aspect. |
| 12 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | Identifies the building where the encounter took place. Needed to determine if the outbreak or cluster is applicable. |
| 13 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Identifies the facility where the encounter took place. Needed to determine if the outbreak or cluster is applicable. |
| 14 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the nurse_unit where the encounter took place. Needed to determine if the outbreak or cluster is applicable. |
| 15 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | Identifies the room where the encounter took place. Needed for reporting aspect. |
| 16 | `MDRO_CAT_NAME` | VARCHAR(100) |  |  | Full name of the mdro category, as defined in the Bedrock MDRO wizard. |
| 17 | `MDRO_CAT_NAME_KEY` | VARCHAR(100) |  |  | Full name of the mdro category, as defined in the Bedrock MDRO wizard, spaces trimmed and all-caps. |
| 18 | `MDRO_NAME` | VARCHAR(100) |  |  | Full name of mdro as defined in Bedrock MDRO Wizard. |
| 19 | `MDRO_NAME_KEY` | VARCHAR(100) |  |  | Full name of mdro as defined in Bedrock MDRO Wizard, spaces trimmed and all-caps. |
| 20 | `MRN` | VARCHAR(100) |  |  | From the alias field on the encntr_alias table. Needed for reporting. |
| 21 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | ID to the Nomenclature table |
| 22 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | Normalcy value for the event |
| 23 | `ORDER_ID` | DOUBLE | NOT NULL |  | Unique key from the orders table. This will be used to assist in determining the uniqueness of the data being considered for insert. |
| 24 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | From code set 1021, populated from CE_MICROBIOLOGY table. |
| 25 | `ORGANISM_OCCURRENCE_NBR` | DOUBLE |  |  | From the CE_MICROBIOLOGY table, used to determine parts of an organism. |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL |  | Unique key from the Person table. |
| 27 | `RESULT_VAL` | VARCHAR(255) |  |  | Stores the clinical_event result |
| 28 | `SPECIMEN_SOURCE_CD` | DOUBLE | NOT NULL |  | Populated from the source_type_cd on the CE_SPECIMEN_COLL table. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

