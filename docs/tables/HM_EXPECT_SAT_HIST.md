# HM_EXPECT_SAT_HIST

> This is a history table for the HM_EXPECT_SATISFIER table.

**Description:** HM EXPECT SAT HIST  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | This is the date/time the action was performed. |
| 2 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | This is the number of the action that was taken. It will be incremented each time a new action is performed. |
| 3 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | This is the action that was performed. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `ENTRY_ID` | DOUBLE | NOT NULL |  | The ID of the entry type from entry_name |
| 11 | `ENTRY_NAME` | VARCHAR(30) | NOT NULL |  | The table name of the ENTRY_ID source |
| 12 | `ENTRY_NBR` | DOUBLE | NOT NULL |  | OBSOLETE on Feature 144577 and subsequent. The entry ID for the specified entry type. This can be a PowerForm form identifier, a Clinical Note document identifier, an order identifier, or an order set identifier. In some cases, this may be the same as the Satisfier Id. |
| 13 | `ENTRY_TYPE_CD` | DOUBLE | NOT NULL |  | OBSOLETE on Feature 144577 and subsequent. A code value from code set 30280 that indicates the method of satisfier entry available from within the Health Maintenance View. Possible conversations are a PowerForm, Clinical Note, Scratch Pad, or EasyScript. Future design will also include PowerNote. |
| 14 | `ENTRY_VALUE` | VARCHAR(255) |  |  | This is a string identifier of the entry type identified by the ENTRY_TYPE_CD. |
| 15 | `EXPECT_ID` | DOUBLE | NOT NULL |  | ID on the EXPECTATION table that indicates which expectation this step belongs to. |
| 16 | `EXPECT_SAT_HIST_ID` | DOUBLE | NOT NULL |  | Logical Primary Key for this table (AK) |
| 17 | `EXPECT_SAT_ID` | DOUBLE | NOT NULL | FK→ | ID on the EXPECT_SATISFIER table that indicates which satisfier this record corresponds to. |
| 18 | `EXPECT_SAT_NAME` | VARCHAR(250) |  |  | This is the name for the expectation satisfier. |
| 19 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Diagnosis to associate to this satisfier. Foreign Key from the Nomenclature table |
| 20 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the satisfier type from parent_entity_name. It is 0 if the satisfier is manual or a clinical event. |
| 21 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The table name of the PARENT_ENTITY_ID source |
| 22 | `PARENT_NBR` | DOUBLE | NOT NULL |  | OBSOLETE on Feature 144577 and subsequent. This is the ID of the satisfier type identified by the PARENT_TYPE_FLAG. If the PARENT_TYPE_FLAG is 2 (indicating a manual satisfier), this field will be 0. |
| 23 | `PARENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | OBSOLETE on Feature 144577 and subsequent. This is a flag indicating what type the satisfier is. It can be a clinical event (0), order or order set (1), or it can be a manual satisfier (2). |
| 24 | `PARENT_VALUE` | VARCHAR(255) |  |  | This is a string identifier of the satisfier type identified by the PARENT_TYPE_FLAG. |
| 25 | `PENDING_DURATION` | DOUBLE | NOT NULL |  | This is the duration after the satisfier is placed in which the expectation will be in a pending status. This field is only valid for order satisfiers. If the order permanently satisfies the step, this value will be 0. |
| 26 | `SATISFIED_DURATION` | DOUBLE | NOT NULL |  | This is the duration that a satisfier will satisfy an expectation. This value is only valid for expectations with an infinite number of steps. |
| 27 | `SATISFIER_MEANING` | VARCHAR(250) |  |  | This is a meaning field that identifies a satisfier. Multiple satisfiers can have the same meaning if they belong to different expectations. Cerner standard satisfiers have a meaning that begins with "CERNER" and client defined expectations are prohibited from utilizing that meaning prefix. |
| 28 | `SAT_STATUS_IND` | DOUBLE | NOT NULL |  | Sat Status IndicatorColumn |
| 29 | `SEQ_NBR` | DOUBLE | NOT NULL |  | This sequence number indicates the order in which the satisfiers should be displayed. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_SAT_ID` | [HM_EXPECT_SAT](HM_EXPECT_SAT.md) | `EXPECT_SAT_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

