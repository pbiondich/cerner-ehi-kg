# BR_MDRO_OUTBREAK

> Defines facility and unit thresholds that will determine whether there is an "outbreak" of a particular MDRO.

**Description:** Bedrock Multi-drug Resistant Organism Outbreak  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_MDRO_OUTBREAK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the br_mdro_outbreak table. |
| 2 | `FACILITY_OCCURRENCE_CNT` | DOUBLE | NOT NULL |  | Number of occurrences at a facility that must be within the facility_time_span to be an outbreak. |
| 3 | `FACILITY_TIME_SPAN_NBR` | DOUBLE | NOT NULL |  | Time span at a facility over which facility_occurrence_cnt must be reached to be an outbreak. |
| 4 | `FACILITY_TIME_SPAN_UNIT_CD` | DOUBLE | NOT NULL |  | The facility time span units of measure. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location for which this outbreak definition is applicable. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The id from the parent_entity_name table. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the parent entity table, which defines the type of outbreak. Valid tables are br_mdro_name, br_mdro_cat, br_mdro_cat_event, br_mdro_cat_organism. |
| 8 | `PROBABILITY_THEORY_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to use probability theory. |
| 9 | `UNIT_OCCURRENCE_CNT` | DOUBLE | NOT NULL |  | Number of occurrences at a unit that must be within the unit_time_span to be an outbreak. |
| 10 | `UNIT_TIME_SPAN_NBR` | DOUBLE | NOT NULL |  | Time span at a unit over which unit_occurrence_cnt must be reached to be an outbreak. |
| 11 | `UNIT_TIME_SPAN_UNIT_CD` | DOUBLE | NOT NULL |  | The unit time span units of measure. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

