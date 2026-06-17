# TRACK_PREARRIVAL_FIELD

> Definitions for data fields for tracking pre-arrivals

**Description:** Track Pre-arrival Field  
**Table type:** REFERENCE  
**Primary key:** `TRACK_PREARRIVAL_FIELD_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_SET` | DOUBLE | NOT NULL |  | Code set column |
| 2 | `CUSTOM_IND` | DOUBLE | NOT NULL |  | Custom indicator col |
| 3 | `DEFAULT_HEIGHT` | DOUBLE | NOT NULL |  | Default height col |
| 4 | `DEFAULT_LABEL` | VARCHAR(40) | NOT NULL |  | Default label col |
| 5 | `DEFAULT_WIDTH` | DOUBLE | NOT NULL |  | Default width col |
| 6 | `FIELD_MEANING` | VARCHAR(12) | NOT NULL |  | Field Meaning col |
| 7 | `FIELD_NAME` | VARCHAR(40) | NOT NULL |  | Field Name |
| 8 | `FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Field type code from code set 20530 |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | ID value from the Parent Entity row |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the Parent Entity (table) for which this data is related. Initial possible tables are CODE_VALUE and TRACK_REFERENCE. |
| 11 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | This field indicates that this TRACK_PREARRIVAL_FIELD entry applies only to a specific tracking group. |
| 12 | `TRACK_PREARRIVAL_FIELD_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACKING_PREARRIVAL_USERFIELDS](TRACKING_PREARRIVAL_USERFIELDS.md) | `TRACK_PREARRIVAL_FIELD_ID` |

