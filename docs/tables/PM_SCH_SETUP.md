# PM_SCH_SETUP

> Stores information for the setup of PM Search.

**Description:** Search setup.  
**Table type:** REFERENCE  
**Primary key:** `SETUP_ID`  
**Columns:** 26  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE |  |  | The parent application number. |
| 2 | `CUTOFF_MODE_FLAG` | DOUBLE | NOT NULL |  | This is the mode that the cut off is set to. It is a flag field with 0,1,2,3 as a value. 0-None, 1-Exact Match, 2-Percentage of Top, 3-Simple Percent Gap. |
| 3 | `EXACT_MATCH` | DOUBLE |  |  | A dynamic cutoff that will return exact matches to the query data plus a specified number of additional records. |
| 4 | `LIMIT_IND` | DOUBLE |  |  | An indicator to limit encounter results. |
| 5 | `LOCKED_IND` | DOUBLE |  |  | Indicates whether or not the record is locked. |
| 6 | `MAX` | DOUBLE |  |  | Maximum return set. |
| 7 | `MAX_ENCNTR` | DOUBLE |  |  | Maximum number of Encounters to return. |
| 8 | `MAX_MPI_RESULTS_NBR` | DOUBLE | NOT NULL |  | The maximum results requested to be returned from an external MPI. |
| 9 | `OPF_IND` | DOUBLE |  |  | Indicates if OPF searches are enabled. |
| 10 | `OPTIONS` | VARCHAR(100) |  |  | Stores a string of 1s and 0s which can be parsed to identify specific options. Used in PDS and MPI. |
| 11 | `PERCENT_TOP` | DOUBLE |  |  | A dynamic cutoff that returns all records with a score greater than or equal to a specified percentage of the match score for the highest scored record. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 13 | `PHONETIC_IND` | DOUBLE |  |  | Indicates if phonetic search will be used. |
| 14 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position_cd of the user the preferences belong to. |
| 15 | `SETUP_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. |
| 16 | `SIMPLE_PERCENT` | DOUBLE |  |  | A dynamic cutoff that returns all records until a gap between the match scores of consecutive records is greater than a specified percentage of the match score for the highest scored record. |
| 17 | `STYLE_FLAG` | DOUBLE |  |  | The type of search. 1-Person search, 2-Patient search, 3-Encounter search, 4-Account search, 5-Guarantor search. |
| 18 | `TASK_NUMBER` | DOUBLE |  |  | The task_number of the application that created the transaction row. |
| 19 | `THRESHOLD` | DOUBLE |  |  | The minimum OPF weight that will be displayed in OPF search results. |
| 20 | `TITLE` | VARCHAR(100) |  |  | Stores the title of the search options window. Obsolete. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `WILDCARD_IND` | DOUBLE |  |  | Indicates if assume wildcards option is on. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PM_SCH_FILTER](PM_SCH_FILTER.md) | `SETUP_ID` |
| [PM_SCH_LIMIT_CODE_VALUE_R](PM_SCH_LIMIT_CODE_VALUE_R.md) | `SETUP_ID` |
| [PM_SCH_RESULT](PM_SCH_RESULT.md) | `SETUP_ID` |

