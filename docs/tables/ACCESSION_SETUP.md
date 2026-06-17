# ACCESSION_SETUP

> Holds the global settings for accession numbers.

**Description:** Accession setup  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_FUTURE_DAYS` | DOUBLE |  |  | The number of days in the future that an accession number can be accepted from the current day. |
| 2 | `ACCESSION_SETUP_ID` | DOUBLE | NOT NULL |  | The system generated number that identifies the row in the table. |
| 3 | `ALPHA_SEQUENCE_LENGTH` | DOUBLE |  |  | Defines the length of the sequence portion of alpha prefixed accession numbers. |
| 4 | `ASSIGN_FUTURE_DAYS` | DOUBLE |  |  | The number of days in the future that an accession number can be assigned. |
| 5 | `DEFAULT_SITE_CD` | DOUBLE | NOT NULL |  | If site prefixes are turned on, this is default that the accession assignment routine will use if the client application does not pass in the facility. |
| 6 | `JULIAN_SEQUENCE_LENGTH` | DOUBLE |  |  | This is the length of the sequence portion of Julian date format accession numbers. |
| 7 | `MANUAL_ASSIGN_IND` | DOUBLE |  |  | Global switch to turn on the ability to manually assign accession numbers. |
| 8 | `SITE_CODE_LENGTH` | DOUBLE |  |  | If site prefixes are turned on, this determines the display length of the site prefixes. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `YEAR_DISPLAY_LENGTH` | DOUBLE |  |  | In the database all four digits of the year portion of an accession number are stored. This field controls how many digits of the year are displayed. Recommended value: 2. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

