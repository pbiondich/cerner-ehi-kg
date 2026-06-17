# BMDI_ASSOCIATION_HINTS

> Hints for Association of Location(Device) to person/alternate record ids

**Description:** BMDI Association Hints  
**Table type:** ACTIVITY  
**Primary key:** `HINT_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `HINT_DT_TM` | DATETIME | NOT NULL |  | Suggests time of association or dissociation of patient with location. |
| 3 | `HINT_ID` | DOUBLE | NOT NULL | PK | Used as a primary key |
| 4 | `HINT_PROCESSING_CD` | DOUBLE | NOT NULL |  | Valid values: ACT, OBSOLETE, ACCEPT, DEFER, MODIFY, REJECT ACT - Start processing hint OBSOLETE - Obsoleted by latest entry for the BMDI location. ACCEPT - Confirm association or dissociation at this BMDI location in BMDI_ACQUIRED_DATA_TRACK table DEFER - Suspend default notification about hint. MODIFY - Retrospectively change association or dissociation connected with this hint. REJECT - Reject further processing on hint. |
| 5 | `HINT_TYPE_CD` | DOUBLE | NOT NULL |  | Valid values: ASSOCIATE, DISSOCIATE. ASSOCIATE when person moves to a BMDI location. DISSOCIATE when person moves out of a BMDI location. |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Specifies the physical location of this person/alternate_record_id. Usually bed_cd with cdf_meaning BED |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies which person is associated with the location. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `UPD_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_id of person from personnel table that caused last insert or update. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `UPD_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BMDI_ACQUIRED_DATA_TRACK](BMDI_ACQUIRED_DATA_TRACK.md) | `HINT_ID` |

