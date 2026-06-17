# OSM_INSURANCE_RELTN

> This table contains the relationship between osm_insurance table and osm_insurance_address table.

**Description:** osm insurance relation table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EMPLOYER_NAME` | VARCHAR(100) |  |  | This is the employer name of the insured person. |
| 2 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | This is the foreign key to the Encounter table. |
| 3 | `OSM_INSURANCE_RELTN_ID` | DOUBLE | NOT NULL |  | This insurance relation id is used to relate the OSM_Insurance table and the OSM_Insurance_address table. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL |  | This column is no longer used. |
| 5 | `PERSON_NAME` | VARCHAR(100) |  |  | Name of the person involved in this OSM Insurance Relationship. |
| 6 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | This is the insurance priority sequence. |
| 7 | `RELATION` | VARCHAR(15) |  |  | This describes the relationship between the insured person and the dependent. |
| 8 | `SSN` | VARCHAR(15) |  |  | This is the social security number. |
| 9 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | This is the insurance type flag. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

