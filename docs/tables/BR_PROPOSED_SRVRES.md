# BR_PROPOSED_SRVRES

> autobuild for service resource hierarchy

**Description:** BEDROCK PROPOSED SERVICE RESOURCE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Activity subtype associated to the service resource |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Activity type associated to the service resource |
| 3 | `AUTOMATED_IND` | DOUBLE | NOT NULL |  | Defined as 1 the automated indicated is defined. |
| 4 | `BR_PROPOSED_SRVRES_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table |
| 5 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Catalog type associated to the service resource |
| 6 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Description for the service resource |
| 7 | `DISPLAY` | VARCHAR(100) | NOT NULL |  | Display for the service resource |
| 8 | `MEANING` | VARCHAR(12) |  |  | The meaning associated to the proposed service resource. |
| 9 | `PARENT_ID` | DOUBLE | NOT NULL |  | The br_proposed_srvres_id the service resource is associated to. |
| 10 | `PROPOSED_IND` | DOUBLE | NOT NULL |  | Defined as 1 the service resource will define in selected. |
| 11 | `SRVRES_LEVEL` | DOUBLE | NOT NULL |  | 1 = department, 2 = section, 3 = subsection, 4 = bench, instrument or rad exam room |
| 12 | `SRVRES_OPTION_NBR` | DOUBLE | NOT NULL |  | The option number for the proposed service hierarchy. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

