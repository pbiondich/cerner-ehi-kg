# CE_SUSCEP_FOOTNOTE

> The ce_suscep_footnote table stores footnotes bound to one or more ce_susceptibility rows. The actual contents of the footnote exist in the long_blob table. The maximum size of a blob stored in this table is 32K compressed. A note must be able to fit i

**Description:** footnotes bound to one or more ce_susceptibility rows  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_LENGTH` | DOUBLE | NOT NULL |  | Size of the uncompressed blob. |
| 2 | `CE_SUSCEP_FOOTNOTE_ID` | DOUBLE | NOT NULL |  | Unique identifier generated for each row of data in the ce_suscep_footnote table. |
| 3 | `CHECKSUM` | DOUBLE | NOT NULL |  | A unique value, created by parsing the contents of the blob, used as a comparison to identify changes to the blob. |
| 4 | `COMPRESSION_CD` | DOUBLE | NOT NULL |  | Specifies type of compression applied to the blob. |
| 5 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 6 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the clinical_event table. |
| 7 | `FORMAT_CD` | DOUBLE | NOT NULL |  | Indicates type of blob. Note that a storage code doesn't exist - all blobs must exist on the long_blob table. Thus only format codes that apply to the storage code "BLOB" are valid here. |
| 8 | `REFERENCE_NBR` | VARCHAR(100) | NOT NULL |  | The combination of the reference nbr and the contributor system code provides a unique identifier to the origin of the data. |
| 9 | `SUSCEP_FOOTNOTE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logical suscep footnote row. There may be more than one row with the same suscep_footnote_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 16 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the End Point of when a row in the table is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

