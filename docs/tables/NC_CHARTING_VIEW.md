# NC_CHARTING_VIEW

> A charting view is a collection of charting sections. A view would represent a set of sections that need documented for a particular workflow. An example would be an Adult Admissions view that contains sections for Vitals, Weight, and Safety. The table includes the view name along with a JSON formatted string containing the grouping of charting sections within the view.

**Description:** Nursing Charting - Charting View  
**Table type:** REFERENCE  
**Primary key:** `NC_CHARTING_VIEW_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CHARTING_VIEW_CLOB` | LONGTEXT |  |  | A JSON formatted string containing the representation of the charting view. This includes the grouping of charting sections in the view along with additional meta data. |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | Contains the date and time the view was created. |
| 5 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for inserting this row on the table |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `NC_CHARTING_VIEW_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the NC_CHARTING_VIEW table. |
| 8 | `ORIG_NC_CHARTING_VIEW_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the Charting Views. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `VIEW_NAME` | VARCHAR(255) | NOT NULL |  | Name that is displayed for the view. |
| 15 | `VIEW_NAME_KEY` | VARCHAR(255) | NOT NULL |  | This field contains the view_name value with all special characters removed and all alpha characters converted to upper case. |
| 16 | `VIEW_NAME_KEY_A_NLS` | VARCHAR(1020) | NOT NULL |  | Stores the corresponding non-English character set values for the view_name_key column. Used to sort correctly internationally. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIG_NC_CHARTING_VIEW_ID` | [NC_CHARTING_VIEW](NC_CHARTING_VIEW.md) | `NC_CHARTING_VIEW_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [NC_CHARTED_VIEW](NC_CHARTED_VIEW.md) | `NC_CHARTING_VIEW_ID` |
| [NC_CHARTING_VIEW](NC_CHARTING_VIEW.md) | `ORIG_NC_CHARTING_VIEW_ID` |

