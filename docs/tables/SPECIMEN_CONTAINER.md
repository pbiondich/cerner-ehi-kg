# SPECIMEN_CONTAINER

> Reference table storing all specimen containers (codeset 2051) used within the Lab and their attributes.

**Description:** Specimen Container  
**Table type:** REFERENCE  
**Primary key:** `SPEC_CNTNR_CD`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIQUOT_IND` | DOUBLE |  |  | An indicator that the container is an aliquot type of container, and not a primary type of container. |
| 2 | `SPEC_CNTNR_CD` | DOUBLE | NOT NULL | PK | The internal number assigned by the system to the Specimen Container. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VOLUME_UNITS` | CHAR(15) |  |  | The units associated with the numeric container volume(s). |
| 9 | `VOLUME_UNITS_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Volume Units. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CONTAINER](CONTAINER.md) | `SPEC_CNTNR_CD` |
| [SPECIMEN_CONTAINER_VOLUME](SPECIMEN_CONTAINER_VOLUME.md) | `SPEC_CNTNR_CD` |

