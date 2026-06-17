# TRACKING_PREARRIVAL_USERFIELDS

> Tracking Pre Arrival information on customizable drop downs

**Description:** Tracking Pre Arrival User Defined Fields  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `TRACKING_PREARRIVAL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to tracking_pre-arrival table |
| 2 | `TRACKING_PREARRIVAL_USRFLD_ID` | DOUBLE | NOT NULL |  | Unique id for the table. Primary Key |
| 3 | `TRACK_PREARRIVAL_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Id for the track_pre-arrival_field record defining this user-defined data |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `USER_DATA_DT_TM` | DATETIME |  |  | The date/time value for this user-defined data if the user_data_type_cd is a date type. |
| 10 | `USER_DATA_IDENT` | DOUBLE | NOT NULL |  | ** OBSOLETE - NO LONGER USED - JANUARY 30, 2008**Identifier from Preferences |
| 11 | `USER_DATA_SEQ` | DOUBLE |  |  | When a TRACK_PREARRIVAL_FIELD_ID occurs more than once for a particular TRACKING_PREARRIVAL_ID this field is used to determine the order in which the data should be displayed on the form. |
| 12 | `USER_DATA_TEXT` | VARCHAR(255) | NOT NULL |  | Short length Free Text |
| 13 | `USER_DATA_TYPE_CD` | DOUBLE | NOT NULL |  | Type of field Code value (20530) |
| 14 | `USER_DATA_VALUE` | DOUBLE | NOT NULL |  | Code_value from one of the code_sets |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACKING_PREARRIVAL_ID` | [TRACKING_PREARRIVAL](TRACKING_PREARRIVAL.md) | `TRACKING_PREARRIVAL_ID` |
| `TRACK_PREARRIVAL_FIELD_ID` | [TRACK_PREARRIVAL_FIELD](TRACK_PREARRIVAL_FIELD.md) | `TRACK_PREARRIVAL_FIELD_ID` |

