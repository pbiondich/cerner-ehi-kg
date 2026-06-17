# CHART_IMMUNIZ_FORMAT

> Immunization Format for Charting

**Description:** Chart Immuniz Format  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_NOTE_IND` | DOUBLE |  |  | Indicates whether or not to show the admin_note for an immunization. |
| 6 | `ADMIN_PERSON_LBL` | VARCHAR(32) |  |  | The label to display next to the admin person |
| 7 | `AMOUNT_IND` | DOUBLE |  |  | Indicates whether or not to display the dosage amount of the immunization. |
| 8 | `AMOUNT_LBL` | VARCHAR(32) |  |  | The label to display next to the dosage amount |
| 9 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the CHART_GROUP table |
| 10 | `DATE_GIVEN_IND` | DOUBLE |  |  | Indicates whether or not to display the date an immunization was given. |
| 11 | `DATE_GIVEN_LBL` | VARCHAR(32) |  |  | The label to display next to the date given |
| 12 | `DATE_MASK` | VARCHAR(50) | NOT NULL |  | The format in which dates in this section will display |
| 13 | `EXP_DT_IND` | DOUBLE |  |  | Indicates whether or not to display the expiration date of an immunization. |
| 14 | `EXP_DT_LBL` | VARCHAR(32) |  |  | The label to display next to the expiration date. |
| 15 | `EXP_TM_IND` | DOUBLE |  |  | Indicates whether or not to display the expiration time of an immunization next to its expiration date. |
| 16 | `LOT_NUM_IND` | DOUBLE |  |  | Indicates whether or not to display the lot # of an immunization substance. |
| 17 | `LOT_NUM_LBL` | VARCHAR(32) |  |  | The label to display next to the lot # |
| 18 | `MANUFACT_IND` | DOUBLE |  |  | Indicates whether or not to display the immunization substance manufacturer. |
| 19 | `MANUFACT_LBL` | VARCHAR(32) |  |  | The label to display next to the substance manufacturer. |
| 20 | `PROVIDER_IND` | DOUBLE |  |  | Indicates whether or not to display the immunization provider. |
| 21 | `PROVIDER_LBL` | VARCHAR(32) |  |  | The label to display next to the provider. |
| 22 | `RESULT_SEQ_IND` | DOUBLE |  |  | Indicates the sequencing of immunizations (1 = reverse chronological; 0 = chronological) |
| 23 | `SITE_IND` | DOUBLE |  |  | Indicates whether or not to display the site the immunizations was administered. |
| 24 | `SITE_LBL` | VARCHAR(32) |  |  | The label to display next to the site. |
| 25 | `TIME_GIVEN_IND` | DOUBLE |  |  | Indicates whether or not to display the time that an immunization was given along with the date given. |
| 26 | `TIME_MASK` | VARCHAR(32) | NOT NULL |  | The format in which dates in this section will display |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `VACCINE_LBL` | VARCHAR(32) |  |  | The label to display next to the vaccine. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

