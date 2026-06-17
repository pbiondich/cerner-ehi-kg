# EMPI_IMPORT_MATCH

> EMPI Import Offsite MPI Extract - The EMPI

**Description:** EMPI Import Match  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `A_PERSON_IDENT` | VARCHAR(255) | NOT NULL |  | The a person match identifier of a match pair. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `B_PERSON_IDENT` | VARCHAR(255) | NOT NULL |  | The b person match identifier of a match pair |
| 8 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the record was created |
| 9 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel ID of the person who created the row in the table |
| 10 | `EMPI_IMPORT_MATCH_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the empi_import_match_table. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EXT_MPI_PERSON_UUID` | VARCHAR(255) |  |  | This is the unique id in the external MPI that links that row. |
| 13 | `EXT_USERNAME` | VARCHAR(50) |  |  | The username of the person who provided the match from the external system. |
| 14 | `GROUP_SCORE_NBR` | DOUBLE |  |  | Group Match Confidence Score |
| 15 | `HUMAN_LINK_IND` | DOUBLE |  |  | A value of 1 means a human performed the link in the foreign system. A value of 0 means a computer assisted link was created in the foreign system. |
| 16 | `HUMAN_MERGE_IND` | DOUBLE |  |  | A value of 1 means a human performed the merge in the foreign system. A value of 0 means a computer assisted merge was created in the foreign system. |
| 17 | `IDENTIFIER_NAME` | VARCHAR(255) | NOT NULL |  | Name of the identifier used for the person match pairs |
| 18 | `LINK_DT_TM` | DATETIME |  |  | The date of the Link in the foreign MPI |
| 19 | `LINK_SCORE_NBR` | DOUBLE |  |  | Link Similarity Score between A and B |
| 20 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 21 | `MERGE_DIRECTION_TXT` | VARCHAR(50) |  |  | Intended merge direction provided by the foreign system (e.g. MERGEINTOA, MERGEINTOB). |
| 22 | `PERSON_COMBINE_BATCH_ID` | DOUBLE | NOT NULL | FK→ | ID of the generated person_combine_batch_id. |
| 23 | `PROCESSED_DT_TM` | DATETIME |  |  | Date and time the row was processed. |
| 24 | `PROCESSED_IND` | DOUBLE | NOT NULL |  | Indicates that the imported match record has been processed. |
| 25 | `PROCESSED_STATUS_CD` | DOUBLE | NOT NULL |  | Contains the status of the processed row. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_COMBINE_BATCH_ID` | [PERSON_COMBINE_BATCH](PERSON_COMBINE_BATCH.md) | `PERSON_COMBINE_BATCH_ID` |

